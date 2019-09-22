from django.shortcuts import render
from game.models import Player, Game, PlayerGameInfo, MIN_VALUE, MAX_VALUE


def get_player(request):
    if 'player' not in request.session:
        player = Player()
        player.save()
        request.session['player'] = player.pk
    else:
        player = Player.objects.get(pk=request.session['player'])
    return player


def get_game_info(game, request):
    """
    Пока что эта функция используется только один раз уже после проверки, что игра существует.
        :param game: объект игры
        :param request: запрос
    """
    player_game_info = PlayerGameInfo.objects.filter(game=game, player=get_player(request))
    if not player_game_info:
        return None
    return player_game_info[0]


def show_home(request):

    game_value = request.GET.get('game_value', None)
    if game_value:
        game_value = int(game_value)

    game = Game.objects.all().oder_by('-id').first()
    min_value = MIN_VALUE
    max_value = MAX_VALUE
    attempts = None
    current_value = None

    if not game:
        if not game_value:
            message = 'Загадайте число!'
        else:
            if MIN_VALUE <= game_value <= MAX_VALUE:
                message = 'Ваша игра началась!'
                current_value = game_value
                game = Game(value=game_value, creator=get_player(request))
                game.save()
            else:
                message = 'Это число не подходит!'
    else:
        if game.creator == get_player(request):
            message = 'Ваша игра идет!'
            current_value = game.value
        else:
            game_info = get_game_info(game, request)
            if game_info:
                attempts = game_info.attempts
                min_value = game_info.min_value
                max_value = game_info.max_value
            else:
                game_info = PlayerGameInfo(game=game, player=get_player(request))

            if game_value:
                if game_value == game.value:
                    message = 'Ура! Вы отгадали число '
                    if not attempts:
                        message += 'с первой попытки! '
                    else:
                        message += f'за {attempts} попыток! '
                    message += 'Начните новую игру!'
                    game.delete()
                else:
                    if min_value <= game_value <= max_value:
                        if game_value < game.value:
                            min_value = game_value + 1
                            game_info.min_value = game_value + 1
                        else:
                            max_value = game_value - 1
                            game_info.max_value = game_value - 1
                        game_info.attempts += 1
                        game_info.save()
                        message = 'Попробуйте еще раз!'
                    else:
                        message = 'Число нахоится вне разрешенного диапазона!'
            else:
                message = 'Попробуйте отгадать число!'
                    
    content = {
        'min_value': min_value,
        'max_value': max_value,
        'current_value': current_value,
        'message': message,
        'attempts': attempts,
    }

    return render(
        request,
        'home.html',
        content
    )                 

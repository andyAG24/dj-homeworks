from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара",
                                     min_value=0,
                                     help_text='Введите сумму больше 0')
    rate = forms.IntegerField(label="Процентная ставка",
                              min_value=0,
                              max_value=100,
                              help_text='Введите ставку (не более 100%))')
    months_count = forms.IntegerField(label="Срок кредита в месяцах",
                                      min_value=1,
                                      help_text='Введите срок больше 0)')

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean(self):
        # общая функция валидации
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')
        months_count = cleaned_data.get('months_count')
        err_msg = 'Значение не может быть отрицательным'

        if rate and rate < 1:
            self.add_error('rate', err_msg)

        if months_count and months_count < 1:
            self.add_error('months_count', err_msg)

        return self.cleaned_data

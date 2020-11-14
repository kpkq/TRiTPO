from django import forms


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(label="Количество", min_value=1, error_messages={"valueError": "Количество книг не "
                                                                                                 "может быть "
                                                                                                 "меньше или равным 0"})

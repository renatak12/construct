from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()

@register.filter
@stringfilter
def formatar_cnpj(cnpj):
    if len(cnpj) == 14:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj

@register.filter
def formatar_telefone(telefone):
    telefone = telefone.replace(' ', '')
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone

@register.filter
def formatar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Remover pontos e traços
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


@register.simple_tag
def tempo_atual():
    return datetime.datetime.now().strftime('%H:%M:%S')
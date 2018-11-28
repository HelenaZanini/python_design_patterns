class CalculadoraDeImpostos():

    def calcular(self, valor, imposto):
        valor_a_pagar = imposto.calcula(valor)
        return valor_a_pagar


def main():
    from strategy_pattern.strategy import ICMS, ISS, PIS

    receita_produto = 50000
    receita_servico = 80000

    calculadora = CalculadoraDeImpostos()

    imposto_produto_icms = calculadora.calcular(receita_produto, ICMS())
    imposto_produto_pis = calculadora.calcular(receita_produto, PIS())
    imposto_produto = imposto_produto_icms + imposto_produto_pis
    receita_produto_liquida = receita_produto - imposto_produto

    imposto_servico_iss = calculadora.calcular(receita_servico, ISS())
    imposto_servico_pis = calculadora.calcular(receita_servico, PIS())
    imposto_servico = imposto_servico_iss + imposto_servico_pis
    receita_servico_liquida = receita_servico - imposto_servico

    print('---------------------------------------------------------------')
    print(f'Produto com receida de: R$ {receita_produto}')
    print(f'ICMS valor de: R$ {imposto_produto_icms}, e PIS valor de: R$ {imposto_produto_pis}')
    print(f'Receita líquida de R$ {receita_produto_liquida}')
    print('---------------------------------------------------------------')
    print(f'Serviço com receida de: R$ {receita_servico}')
    print(f'ISS valor de: R$ {imposto_servico_iss}, e PIS valor de: R$ {imposto_servico_pis}')
    print(f'Receita líquida de R$ {receita_servico_liquida}')


if __name__ == '__main__':
    main()
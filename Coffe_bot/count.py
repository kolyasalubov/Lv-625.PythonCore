
def count_menu (str):
    count_latte=str.count('latte')
    count_cappucino=str.count('cappucino')
    count_americano=str.count('americano')

    answer_order=''
    if count_latte>0: answer_order+=(f'{count_latte} Латте \n')
    if count_cappucino>0: answer_order+=(f'{count_cappucino} Каппучино \n')
    if count_americano>0:answer_order+=(f'{count_americano} Американо \n')

    sum=count_americano*25+count_cappucino*35+count_latte*35
    answer_order+=(f'на сумму: {sum} гривен')
    return answer_order

vegetables_kg_lv = float(input())
fruits_kg_lv = float(input())
vegetables = int(input())
fruits = int(input())
bgn_to_euro = 1.94

total_euro = (vegetables * vegetables_kg_lv + fruits * fruits_kg_lv) / bgn_to_euro

print(format(total_euro, '.2f'))
import json
m_f = open("Test7.txt", "+r",encoding="utf-8")
average_profit = 0
firm_dict = {}
profit_dict = {}
for i in m_f.readlines():
    firm, tipe, money_up, money_down = i.split()
    if int(money_up)> int(money_down):
        average_profit += (int(money_up)-int(money_down))
    firm_dict[firm] = (int(money_up)-int(money_down))
profit_dict["Average profit"] = average_profit
final_list = [firm_dict, profit_dict]
print(final_list)
with open("Test8.json", "w", encoding="utf-8") as f_f:
    json.dump(final_list, f_f, ensure_ascii=False, indent=4)
m_f.close()
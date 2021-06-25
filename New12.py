class GoldInvoice:
    def __init__(self,id,name,qty,rate,weight,pwc,pdis):
        self.item_id = id
        self.item_name = name
        self.item_qty = qty
        self.item_rate = rate
        self.item_weight = weight
        self.item_pwc = pwc
        self.item_pdis = pdis

    def calc_item_price_exGST(self,gold_invoice_list,item_id_choice):
        for i in gold_invoice_list:
            if i.item_id == item_id_choice:
                item_cost = i.item_qty * i.item_rate * i.item_weight
                pwc = item_cost * (i.item_pwc/100)
                pd = item_cost * (i.item_pdis/100)
                result = item_cost + pwc - pd
                return result

    def calc_item_price_inGST(self,gold_invoice_list,item_id_choice):
        for i in gold_invoice_list:
            if i.item_id == item_id_choice:
                item_cost = i.item_qty * i.item_rate * i.item_weight
                pwc = item_cost * (i.item_pwc/100)
                pd = item_cost * (i.item_pdis/100)
                gst = item_cost * (3/100)
                result = item_cost + pwc - pd + gst
                return result

if __name__ == '__main__':
    l = []
    n = int(input())
    for i in range(n):
        id = float(input())
        name = input()
        qty = float(input())
        rate = float(input())
        weight = float(input())
        pwc = float(input())
        pdis = float(input())
        l.append(GoldInvoice(id,name,qty,rate,weight,pwc,pdis))

    item_id = int(input())
    g = GoldInvoice(0,"",0,0,0,0,0)
    res1 = g.calc_item_price_exGST(l,item_id)
    res2 = g.calc_item_price_inGST(l,item_id)
    print(round(res1,2))
    print(round(res2,3))
"""
📝 Product name: Apple

▪️ Energy: 1000 kcal
▪️ Protein: 1000 g
▪️ Lipid: 1000 g
▪️ Alcohol: 1000 g
▪️ Caffeine: 1000 g
▪️ Sugar: 1000 g
▪️ Calcium: 1000 g
▪️ Iron: 1000 g
▪️ Magnesium: 1000 g
▪️ Phosphorus: 1000 g
▪️ Potassium: 1000 g

"""


PRODUCTS_UZB = {
    "apples": "olmalar",
    "apricots": "o'rik",
    "avocados": "avakado",
    "bananas": "banan",
    "blackberries": "maymunjon",
    "blueberries": "ko'katlar",
    "cantaloupes": "qovunlar",
    "carrots": "sabzi",
    "cherries": "gilos",
    "coconuts": "hindiston yong'og'i",
    "figs": "anjir",
    "garlic": "sarimsoq",
    "grapefruits": "greyfurtlar",
    "grapes": "uzum",
    "kiwifruit": "kivi mevasi",
    "lemons": "limon",
    "limes": "ohak",
    "mangos": "mango",
    "melon": "qovun",
    "olives": "zaytun",
    "onion": "piyoz",
    "oranges": "apelsinlar",
    "peaches": "shaftoli",
    "pears": "nok",
    "pepper": "qalapmir",
    "pineapples": "ananaslar",
    "plums": "olxo'ri",
    "pomegranates": "anorlar",
    "potato": "kartoshka",
    "raspberry": "malina",
    "strawberries": "qulupnay",
    "tomatoes": "pomidor",
    "watermelons": "tarvuzlar",
}


NUTRITIONS_NAME = {
    "Protein": "Protein",
    "Total lipid (fat)": "Umumiy lipid (yog')",
    "Energy": "Energiya",
    "Alcohol, ethyl": "Alkogol, etil",
    "Caffeine": "Kofein",
    "Sugars, total including NLEA": "Shakar",
    "Calcium, Ca": "Kaltsiy, Ca",
    "Iron, Fe": "Temir, Fe",
    "Magnesium, Mg": "Magniy, Mg",
    "Phosphorus, P": "Fosfor, P",
    "Potassium, K": "Kaliy, K",
}


async def create_text(product_name, data: dict) -> str:
    if data.get("status"):
        text = f"📝 Mahsulot nomi: <b>{PRODUCTS_UZB.get(product_name.strip()).title()}</b>" + "\n\n"
        details = data.get(product_name)
        for name in details.keys():
            nutrient_name = details[name].get('nutrientName')
            text += f"▪️ <b>{NUTRITIONS_NAME.get(nutrient_name)}</b>:  {details[name].get('value')} {details[name].get('unitName')}\n"
        text += "\n👉 <a href='https://t.me/define_contentbot'>@define_contentbot</a>"
        return text
    return None

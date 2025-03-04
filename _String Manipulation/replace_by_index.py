# Четем оригиналния YML файл
file_path = "/mnt/data/config (3).yml"

with open(file_path, "r", encoding="utf-8") as file:
    yml_content = file.read()

# Превеждаме съдържанието, като оставяме непроменени частите с %
translations = {
    "Default language file": "Файл с езикови настройки по подразбиране",
    "Hides the purchase thank you message in the console.": "Скрива съобщението за благодарност след покупка в конзолата.",
    "currency": "валута",
    "allow pick": "разреши избор",
    "default selection": "избор по подразбиране",
    "vault symbol": "символ на хранилището",
    "vault symbol overrides": "символът на хранилището замества",
    "black listed": "в черния списък",
    "format": "формат",
    "language": "език",
    "country": "държава",
    "abbreviate numbers": "съкратени числа",
    "hide vault symbol": "скриване на символа на хранилището",
    "strip ending zeroes": "премахване на крайни нули",
    "tight currency symbol": "плътен символ на валута",
    "use grouping": "използване на групиране",
    "hide space between in currency": "скриване на интервала в валутата",
    "command aliases": "псевдоними на команди",
    "main": "главна",
    "subcommands": "подкоманди",
    "active": "активни",
    "cart": "количка",
    "admin": "администратор",
    "ban": "забрана",
    "bids": "оферти",
    "confirm": "потвърждение",
    "expired": "изтекли",
    "filter": "филтър",
    "markchest": "маркиран сандък",
    "price limit": "лимит на цена",
    "payments": "плащания",
    "request": "заявка",
    "search": "търсене",
    "sell": "продажба",
    "stats": "статистики",
    "toggle list info": "превключване на информацията в списъка",
    "transactions": "транзакции",
    "unban": "отмяна на забрана",
}

# Замяна на английските термини с български
for eng, bg in translations.items():
    yml_content = yml_content.replace(eng, bg)

# Записваме преведения файл
translated_file_path = "/mnt/data/config_translated.yml"
with open(translated_file_path, "w", encoding="utf-8") as file:
    file.write(yml_content)

translated_file_path

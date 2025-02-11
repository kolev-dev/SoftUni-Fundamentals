def progress_bar(percent: int) -> str:

    percent_divided_by_10 = percent // 10
    not_loaded = 10 - percent_divided_by_10

    #this is string
    percent_string = "%" * percent_divided_by_10
    dot_string = "." * not_loaded

    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    return  f"{percent}% [{percent_string}{dot_string}]\nStill loading..."



loading_percent = int(input())
print(progress_bar(loading_percent))

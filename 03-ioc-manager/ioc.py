import json
from pathlib import Path 
class IOCManager:
    def __init__(self, file_path="iocs.json"):
        self.file_path = Path(file_path)
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.iocs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.iocs = []


    def save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.iocs, f, indent=4)
    def add_ioc(self,indicator, ioc_type, note=""):
        self.newiocs = {"indicator": indicator, "type": ioc_type, "note" : note}
        self.iocs.append(self.newiocs)
        self.save()

    def search_ioc(self, keyword):

        
        for ioc in self.iocs:
            if keyword.lower() in ioc["indicator"].lower() or keyword.lower() in ioc["type"].lower() or keyword.lower() in ioc["note"].lower():
                print(f" Da tim thay IOC co chua tu {keyword}: {ioc} ")

    def remove_ioc(self, indicator):
        for ioc in self.iocs:
            if indicator == ioc["indicator"]:
                self.iocs.remove(ioc)
                self.save()
                print(f" Da xoa IOC voi indicator: {indicator} ")



if __name__ == "__main__":
    ioc_manager = IOCManager()
    while True:
        print("Them ioc : 1")
        print("Tim ioc : 2")
        print("Xoa ioc : 3")
        print("Thoat : 4")
        choice = input("Chon thao tac: ")
        if choice == "1":
            indicator = input("Nhap indicator: ")
            ioc_type = input("Nhap type: ")
            note = input("Nhap note: ")
            ioc_manager.add_ioc(indicator, ioc_type, note)
        elif choice == "2":
            keyword = input("Nhap tu khoa tim kiem: ")
            ioc_manager.search_ioc(keyword)
        elif choice == "3":
            indicator = input("Nhap indicator can xoa: ")
            ioc_manager.remove_ioc(indicator)
        elif choice == "4":
            break


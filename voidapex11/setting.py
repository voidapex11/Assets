import json
class setting:
  def get(settingName: str, defaltData=None):
    tf = {settingName: defaltData}
    try:
      with open("Assets/settings.json", "r") as file:
        try:
          tf = json.load(file)
        except:
          tf = {}

        try: 
          if tf[settingName]:
            pass
        except:
          tf[settingName] = defaltData

        with open("Assets/settings.json", "w") as file:      
          json.dump(tf, file)

    except:
      with open("Assets/settings.json", "x") as file:
        json.dump(tf, file, indent= 2)

    with open("Assets/settings.json", "r") as read_file:
      data = json.load(read_file)
      return data[settingName]
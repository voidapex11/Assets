class setting:
  def __init__(self, settingName, defaltData=None)
    try:
      with open("assets/settings.json", "r") as file:
        try:
          tf = json.load(file)
        except:
          tf = {}

        try: 
          if tf[settingName]:
            settings = tf
        except:
          tf[settingName] = defaltData

        with open("assets/settings.json", "w") as file:      
          json.dump(tf, file)

    except:
      with open("assets/settings.json", "x") as file:
        json.dump(settings, file, indent= 2)

    with open("assets/appData.json", "r") as read_file:
      data = json.load(read_file)
      return data[settingName]
if message.content.startswith("$sheetlog"):
        
      with open("count.json","r+") as f:
        print("Found file")
        obj = json.load(f)
        obj2 = obj["data"]
        line = obj2[-1]
        vals = []
        print(line)
        f.close()
      count = line
      await channel.send("Finding row")
      count2 = count
      
      while True:
        count2 = count2 + 1
        cell = sheet.cell(count2,1).value
        if type(cell) == str and len(cell) > 1:     
          continue
        else:
          row = count2
          await channel.send("Available row: {}".format(count2))
          break
      user = message.author

      Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)    
      await channel.send(embed=Embed)
      msgstr = str(message.content)
      print(msgstr)
      
      while True:
        insert = row
        insert = int(insert)
        msg = await client2.wait_for('message')
        
        if msg.author == message.author:
          content = msg.content
          string = str(content)
          split = string.split(",")
          log_data = split
          insertRow = log_data
          user = str(user)
          
          try:
            insertRow[3] = float(insertRow[3])
            print("row3")
            insertRow[4] = float(insertRow[4])
            #print("row4")
            insertRow[5] = float(insertRow[5])
            print("done int conv")
          except ValueError:
            await channel.send("`Error converting to int, most likely data incomplete.`")
            Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)    
            await channel.send(embed=Embed)
            continue
          print(len(insertRow))
          
          if len(insertRow) < 10 and len(insertRow) > 7:
            print(len(insertRow))
            await channel.send("`Experimental feature triggered due to incomplete list...`")
            print("experimental")
            for i in range(11):
              if len(insertRow) == i:
                print(i)
                num = 11 - i
                print("Num, {}".format(num))
            if num > 0:
              for i in range(num):
                print("No data")
                insertRow.append("No data")
                continue
          if len(insertRow) < 8:
            await channel.send("`Incomplete data list.`")
            Embed = discord.Embed(title="**Log Data Required**",description="Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.", color=0xe23434)
            await channel.send(embed=Embed)
            continue
          
          sheet.insert_row(insertRow,insert)
          datainsert = []
          counter = len(insertRow)
          for i in range(0,counter):  
            datainsert.append(insertRow[i])
          user = message.author
          user2 = user.id
          user4 = str(user2)
          user3 = str(user)
          channel2 = message.channel
          channel3 = str(channel2)
          time2 = date.today()
          time3 = str(time2)
          datainsert.append(user3)
          datainsert.append(user4)
          datainsert.append(time3)
          datainsert.append(channel3)     
          print(datainsert,"f")
          datasheet.insert_row(datainsert)
          
          Embed = discord.Embed(title="**Data Logged**",description="Logged by {}".format(user), color=0xe23434)    
          await channel.send(embed=Embed)
          msgdump = client2.get_channel(852563303082623016)
          await msgdump.send("```diff \n Logged by {}. Row: {}. Logged data: \n {}```".format(user,count2,datainsert))
          
          with open("count.json","r+") as f:
            filename = "count.json"
            print("Found file")
            obj = json.load(f)
            obj2 = obj["data"]
            line2 = count2
            vals = []
            obj2.append(line2)
            print(line2)
            f.close()
          write(obj,filename)
          catid = channel.category_id
          if catid == 810144233616441345:
            await channel.send("Deleting channel, ticket has been logged")
            await channel.delete()
          break

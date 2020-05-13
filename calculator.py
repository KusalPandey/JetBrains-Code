class SmartCalculator:
    command_list = ("help", "exit")
    variable_data = dict()

    def commands(self, command):
        if command not in self.command_list:
            return "Unknown command"
        else:
            if command == "exit":
                print("Bye!")
                exit(0)
            elif command == "help":
                return '''This is a state of the art modern calculator,
Created to perform most type of calculations'''

    def storage(self, data):
        key = data[0]
        values = data[-1]
        self.variable_data[key] = values
        self.main()

    def calculate(self, information):
        try:
            data = information.split(' ')
            for info in data:
                if info in self.variable_data:
                    temp = data.index(info)
                    data[temp] = self.variable_data[info]
            data = " ".join(data)
            b = eval(data)
            b = int(b)
            return b
        except NameError:
            try:
                for info in information:
                    if info in self.variable_data:
                        temp = information.index(info)
                        information = information.replace(info, self.variable_data[info])
                c = eval(information)
                c = int(c)
                return c
            except:
                return "Unknown variable"
        except SyntaxError:
            return "Invalid expression"

    def assign(self, information):
        data = information.split('=')
        if not data[0].isalpha():
            return "Invalid identifier"
        if data[1].isalpha():
            if data[1] in self.variable_data:
                self.variable_data[data[0]] = self.variable_data[data[1]]
                self.main()
            else:
                return "Unknown variable"
        if not data[1].isalpha() and not data[1].isdigit():
            return "Invalid assignment"
        self.storage(data)

    def enter(self, information):
        result = 0
        data = information
        if data.startswith("/"):
            data = data.replace(" ", '')
            command = data.replace("/", "")
            result = self.commands(command)
        elif "=" in data:
            count = 0
            for yea in data:
                if yea == "=":
                    count += 1
            if count >= 2:
                return "Invalid assignment"
            else:
                data = data.replace(" ", '')
                return self.assign(data)
        else:
            result = self.calculate(data)
        return result

    def main(self):
        while True:
            insert = input()
            if len(insert) == 0:
                continue
            else:
                print(self.enter(insert))


if __name__ == "__main__":
    run = SmartCalculator()
    run.main()

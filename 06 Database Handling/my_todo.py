import db_helper

def main():
    run = 1
    db_helper.create_table()
    while run:
        print("\n*** TO DO CONSOLE APPLICATION ***")
        print('1.Insert new task in todo\n'\
              '2.Display the todo tasks\n'\
              '3.Delete the todo task\n'\
              '4.Exit\n')
        ch = input("Enter your choice : ")
        if ch == "1" :
            t_id = int(input("Enter the task id   : "))
            task = str(input("Enter you todo task : "))
            db_helper.data_entry(t_id,task)
        elif ch == "2":
            db_helper.print_data()
        elif ch == "3":
            index = int(input("Enter the ID of todo task to be deleted : "))
            db_helper.delete_task(index)
        elif ch == "4":
            run = 0
        else :
            print("Please choose valid choice ")

    db_helper.close()

if __name__ == '__main__':
    main()
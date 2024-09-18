print("==================")
choice = int(input("Press 1 to begin, 2 to end program. "))

if choice == 1:
    destination = input("Do you have a destination in mind? Yes/No ").lower()

    if destination == "yes" or destination == "y":
        transport = str(
            input("What transportation would you like to book? [A]. Plane [B]. Train [C]. Car  ")).lower()

        if transport == "a" or transport == "plane":
            passengers = int(input("How many people are travelling in your group? "))
            for i in range(passengers):
                last_Name = input("Enter your last name: ")
                p_num = str(input("Enter your phone number: "))
                print(f"Passenger Manifest uploaded! Registration successfully reserved! Welcome aboa1rd {last_Name}, your reservation # is rn#{p_num}. ")


        elif transport == "b" or transport == "train":
            print("This is a member-only zone.")
            username = input("====Enter your username: ").lower()
            password = input("Enter your password: ")
            tries = 2

            while username != "kate layton" and password != "panCake2024" and tries != 0:
                print("Invalid login. Try again. ")
                username = input("====Enter your username: ").lower()
                password = input("Enter your password: ")

                tries -= 1

                if tries == 0:
                    print("Connection timed out. Please try again. ")

                elif username == "kate layton" and password == "panCake2024":
                    p_num = int(input("Enter your phone number: "))
                    print(f"Your booking itinerary has been reserved and your reservation number is #2024{p_num}.")

        elif transport == "c" or transport == "car":

            birth_year = int(input("Enter your birth year: "))
            #today's current year is 2024
            age = 2024 - birth_year


            while age > 21:
                ppl = int(input("How many people will be travelling with you? "))
                type = input("Choose 1: a. luxury || b. economy || c. off-road? ").lower()

                if ppl > 8:
                    print("We do not have a vehicle to accomodate this party size, we are sorry. Please try again. ")

                elif ppl <= 0:
                    print("Please enter the number of people travelling with you. ")

                elif ppl >= 5:
                    print("You've been assigned a 2023 Toyota Sienna! ")
                    break

                elif ppl >= 3 and type == "economy" or type == "b":
                    print("You've been assigned a 2023 Kia Soul! ")
                    break

                elif ppl >= 1 and type == "economy" or type == "b":
                    print("You've been assigned a 2023 Hyundai Elantra! ")
                    break

                elif ppl >= 2 and type == "luxury" or type == "a":
                    print("You've been assigned a 2023 BMW Gran Coupe! ")
                    break


                elif ppl >= 4 and type == "luxury" or type == "a":
                    print("You've been assigned a 2023 Mercedez-Benz G-Class Wagon! ")
                    break

                elif type == "off-road" or "c":
                    print("You've been assigned a 2023 Jeep Wrangler! ")
                    break


    else:
        print("You have a chance to participate in a chance to win a free trip to Nepal for 2 people! ")
        print("In order to win the free trip, you must be able to answer 6 trivia questions about the world's history in a row! ")
        ready = input("Are you ready? Yes/No ").lower()

        while ready != "no" or ready != "n":

            tries = 5

            print("There were also female gladiators in Ancient Rome! They were rare compared to their male-counterparts. What were they called? ")
            answer1 = input("[A]. Amazonians [B]. Gladiatrix [C]. Ninjas [D]. Centuria  ").lower()

            while answer1 == "b":
                print("You are right! Female gladiators were known as gladiatrix and were as fierce as their male-counterparts! ")
                print("===================")
                print("The Silk Road is a Eurasian road network that made trade industry hugely successful, mainly a boom in the spice industry. Which country first started the development of this 4,000mi trade route? ")
                answer2 = input("[A]. Italy [B]. Egypt [C]. China [D]. India ")

                while answer2 == "c":
                    print("Great job! Silk Road first started in China, and extended the roads to as far as India, as the spice and herb were a popular demand within India and China. ")
                    print("===================")
                    print("This city is famous for streets being underwater and people getting around in boats rather than cars. Which city is it? ")
                    answer3 = input("[A]. Dakar [B]. Venice [C]. Oslo [D]. Stockholm  ").lower()

                    while answer3 == "b":
                        print("Venice is sinking every year by 1-3 millimeter. The city is 72 inches lower than it was on 421 AD! ")
                        print("===================")
                        print("George Washington opened his very first distillery at which location? ")
                        answer4 = input("[A]. St. Louis  [B]. Washington, DC [C]. Texas [D]. Mount Rushmore ").lower()

                        while answer4 == "d":
                            print("George Washington introduced modern day drinking at the bar and restaurant setting, opening his first distillery in the early 1700's! ")
                            print("===================")
                            print("Torii is a structure that withstood the power of atomic bomb, earthquake and tsunami. Where is this structure located? ")
                            answer5 = input("[A]. Nagasaki [B]. Bangkok [C]. Canberra [D]. Taipei City ").lower()

                            while answer5 == "a":
                                print("Nagasaki faced an atomic bomb attack during the WWI and an earthquake followed by a tsunami in 2011. Through it all, the torii stood. ")
                                print("===================")
                                print("Which country has been the world's number 1 supplier for coffee? ")
                                answer6 = input("[A]. Vietnam [B]. Ecuador [C]. Colombia [D]. Brazil ").lower()

                                while answer6 == "d":
                                    print("Brazil has produced nearly 3 mil tonnes of coffee beans in 2016! They supply the most coffee beans in the world, followed by Vietnam and Colombia. ")
                                    print("===================")
                                    print("===================")
                                    print("===================")
                                    print("CONGRATULATIONS YOU WON A FREE TRIP FOR 2 TO NEPAL! ")
                                    date = input("Enter the date you want to go and a return date in this format: MM/YYYY to MM/YYYY ")

                                    print(f"Your trip begins on {date}! Thank you for using our services and we wish you safe travels! ")
                                    break

                        print("Sorry, better luck next time. ")
                        break
                    print("Sorry, better luck next time. ")
                    break
                print("Sorry, better luck next time. ")
                break
            print("Sorry, better luck next time. ")
            break



else:
    print("Connection timed out. Please refresh.")

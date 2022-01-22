'''
Age factors
Travveled over seas or out of state in past 2-3 weeks(yes=most likely)
Any mass gatherings attended(yes=most likely)
Symptoms:
Cough
Runny nose
Sneezing
Sore throat
Shortness of breath
Fever
Night sweats
Chills
Headache
Loss of smell
Fatigue
How long symptoms take to show up
Doses of vaccination
tiredness
red eyes
Cancer
Chronic kidney disease
Chronic liver disease
Chronic lung diseases
Dementia or other neurological conditions
Diabetes (type 1 or type 2)
Down syndrome
Heart conditions
HIV infection
Immunocompromised state (weakened immune system)
Mental health conditions
Overweight and obesity
Sickle cell disease or thalassemia
Smoking, current or former
Substance use disorders
Tuberculosis
'''
def travel(x):
  print(x)
    
def symptoms():
  a="yes"
  b="no"
  d="Delta Variant of COVID"
  o="Omnicron Variant of COVID"
  f="Flu"
  c="Common Cold"
  acns=["YES","YEs","Yes","yes","NO","No","no"]
  print("Please respond to the following questions in a Yes/No format only")
  cough = str(input("Have you been coughing frequently?"))
  if cough not in acns:
    print("Pleast write the question again in the proper format.")
    symptoms()
    return
  else:
   runny_nose = str(input("Is your nose runny?"))
   if runny_nose not in acns:
    print("Pleast write the question again in the proper format.")
    symptoms()
    return
   else:
     sneezing = str(input("Have you been sneezing frequently?"))
     if sneezing not in acns:
      print("Pleast write the question again in the proper format.")
      symptoms()
      return
     else:
      shortness_of_breath = str(input("Do you have any difficulty in  breathing?"))
      if shortness_of_breath not in acns:
        print("Pleast write the question again in the proper format.")
        symptoms()
        return
      else:
       sore_throat = str(input("Do you have a sore throat?"))
       if sore_throat not in acns:
        print("Pleast write the question again in the proper format.")
        symptoms()
        return
       else:
        fever = str(input("Do you have a fever?"))
        if fever not in acns:
          print("Pleast write the question again in the proper format.")
          symptoms()
          return
        else:
         night_sweats = str(input("Do you sweat in the night?"))
         if night_sweats not in acns:
           print("Pleast write the question again in the proper format.")
           symptoms()
           return
         else:
          chills = str(input("Have you been getting chills recently?"))
          if chills not in acns:
            print("Pleast write the question again in the proper format.")
            symptoms()
            return
          else:
           headache = str(input("Have you been getting headaches recently?"))
           if headache not in acns:
             print("Pleast write the question again in the proper format.")
             symptoms()
             return
           else:
             loss_of_smell = str(input("Have you lost your sense of smell?"))
             if loss_of_smell not in acns:
               print("Pleast write the question again in the proper format.")
               symptoms()
               return
             else:
              fatigue = str(input("Have you been feeling tired and getting a lot of fatigue?"))
              if fatigue not in acns:
                print("Pleast write the question again in the proper format.")
                symptoms()
                return
              else:
               while True:
                try:
                 Time = int(input("How long did it take for symptoms to show?"))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                if Time < 0:
                 print("Sorry, your response must not be negative.")
                 continue
                else:
                 break
               listof=["Cancer","Chronic kidney disease","Chronic Lung disease","Dementia","Neurological Conditions","Diabetes","Down Syndrome","Heart conditions","HIV","Weakened Immune system","Mental Health conditions","Overweight and obesity","Sickle cell disease","smoking, current of former","substance use disorders","Tuberculosis"]
               print(listof)
               dis=str(input("Have you got any of these diseases[Yes/No]?"))
              if dis=="yes" and cough=="yes" and runny_nose=="yes" and sneezing=="yes" and shortness_of_breath=="yes" and sore_throat=="yes"and fever=="yes" and night_sweats=="yes" and chills=="yes" and headache=="yes" and loss_of_smell=="yes"and fatigue=="yes":
                print("You are in an extreme chronic condition and so go to a doctor as soon as possible.")
                travel()
            
              elif dis=="yes" and cough=="no" and runny_nose=="no" and sneezing=="no" and shortness_of_breath=="no" and sore_throat=="no" and fever=="no" and night_sweats=="no" and chills=="no" and headache=="no" and loss_of_smell=="no" and fatigue=="no":
                print("Be careful as you are in dangerous condition, and maintain COVID protocols all the time to ensure your safety.")
                travel()
            
               elif dis=="no" and cough=="yes" or runny_nose=="yes" or sneezing=="yes" or shortness_of_breath=="yes" or sore_throat=="yes"or fever=="yes" or night_sweats=="yes" or chills=="yes" or headache=="yes" or loss_of_smell=="yes" or fatigue=="yes":
                print("Please continue")
                if cough==a and runny_nose==a and sneezing==b and shortness_of_breath==a and sore_throat==a and fever==a and night_sweats==b and chills==a and headache==a and loss_of_smell==a and fatigue==a and Time==4 or Time==5:
                print("You are most likely to have Delta Variant of COVID")
                travel(d)
                elif cough==a and runny_nose==a and sneezing==a and shortness_of_breath==b and sore_throat==a and fever==a and night_sweats==a and chills==a and headache==a and loss_of_smell==a and fatigue==a and Time==2 or Time==3:
                print("You are most likely to have Omnicron Variant of COVID")
                travel(o)
                elif cough==a and runny_nose==a and sneezing==b and  shortness_of_breath==b and sore_throat==a and fever==a and night_sweats==b and chills==a and headache==a and loss_of_smell==b and fatigue==a and Time==2 or Time==4:
                print("You are most likely to have the flu")
                travel(f)
                elif cough==a and runny_nose==a and sneezing==a and shortness_of_breath==b and sore_throat==a and fever==a and night_sweats==b and chills==b and headache==a and loss_of_smell==b and fatigue==a and Time==1 or Time==3:
                print("You are most likely to have the common cold")
                travel(c)
                else:
                 if cough==b and runny_nose==a and sneezing==a and shortness_of_breath==b and sore_throat==a and fever==b and night_sweats==b and chills==b and headache==a and loss_of_smell==b and fatigue==a and Time==2 or Time==3:
                  print("You might have Omnicron Variant of COVID")
                  travel(o)
                 elif cough==a and runny_nose==b and sneezing==b and shortness_of_breath==b and sore_throat==b and fever==a and night_sweats==b and chills==a and headache==a and loss_of_smell==b and fatigue==a and Time==2 or Time==4:
                  print("You might have the flu") 
                  travel(f)
                 elif cough==a and runny_nose==a and sneezing==b and           shortness_of_breath==b and sore_throat==a and fever==a and    night_sweats==b and chills==b and headache==b and loss_of_smell==a and fatigue==b and Time==1 or Time==3:
                   print("You might have the common cold")
                   travel(c)
               elif dis=="no" and cough=="no" and runny_nose=="no" and sneezing=="no" and shortness_of_breath=="no" and sore_throat=="no" and fever=="no" and night_sweats=="no" and chills=="no" and headache=="no" and loss_of_smell=="no" and fatigue=="no":
                print("You are in no danger, but be careful and follow all COVID protocols to ensure your safety and the safety of others around you")
                travel() 

    
print("Welcome to the COVID Predictor")
Name=str(input("What is your name?"))
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        #age was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break
if age>=60:
  dose=int(input("How many doses  of vaccination have you taken?"))
  if dose<2:
    print("Please take",str(2-dose),"doses, along with a booster dose")
    symptoms()
  elif dose==2:
    print("Good Job, but take a booster dose to increase your safety")  
    symptoms() 
  else:
    print("Great Job, now follow all COVID precautions like putting on mask and so on.")
    symptoms()
else:
  print("Please take the required amount of doses for your age, and follow corona protocols at all times.")
  symptoms()
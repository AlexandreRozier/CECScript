# ZEPfinder

Here is a little project I made for a social organization called [CEC](http://cec.via.ecp.fr/), who adresses school dropout in Paris.

This solution helps to determine whether a pupil is located in a deprived area, thanks to the [ZEP](https://sig.ville.gouv.fr/adresses/recherche) map provided by the French government.

###How does it work ?

Providing an Excel sheet with the adresses of the student, one should have three columns : the number, the name and the zipcode of each adress. Then export the Excel sheet in CSV format, call it **adresses.csv** and save it in the same file than the script.

Finally, one just has to launch this script to get a **result.txt** file, containing the adresses ordered in two categories : ZUP or not ZUP.

Hope this will help !

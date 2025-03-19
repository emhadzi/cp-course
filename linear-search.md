LINEAR SCAN / COMPLETE SEARCH

Usual linear search, running sum/min/max
Iterate forward, backward, with step, ...

https://cses.fi/problemset/task/1069
https://pdp-archive.github.io/27-PDP/a-xxx-statement
https://pdp-archive.github.io/28-PDP/camp-j-metoxes2-statement

Can be extended for pairs (i, j), triplets(i, j, k)..., iterating over all nC2, nC3...

2Sum O(n^2) https://pdp-archive.github.io/26-PDP/c-sumpair-statement
https://leetcode.com/problems/island-perimeter/description/

Δεδομένου ένος πίνακα *n* αριθμών, συχνά αρκεί να εξετάσουμε κάθε στοιχείο του πίνακα από μία φορά για να απαντήσουμε σε κάποια βασική ερώτηση.

Για παράδειγμα αν χρειάζεται να βρούμε το άθροισμα των στοιχείων πίνακα a:

`
    int sum = 0;
    for(int i = 0; i < n; i++)
        sum += a[i];
`
Για να αναφερθούμε σε κάθε στοιχείο του a χρησιμοποιηούμε την μεταβλητή *i* που λειτουργεί ως δείκτης (index). 
Ο δείκτης αρχικοποιείται με την τιμή 0 καθώς αυτή είναι η θέση του πρώτου στοιχείου και αυξάνεται κατά 1 όσο δεν έχει ξεπεράσει το τελευταίο στοιχείο που βρίσκεται στην θέση *n-1*


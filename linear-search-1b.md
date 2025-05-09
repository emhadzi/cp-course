Γραμμική επεξεργασία (Μέρος Β)
===

Είδαμε πώς μπορούμε να λύσουμε προβλήματα για ένα σύνολο, χτίζοντας σταδιακά την απάντηση από κάθε στοιχείο

Παρακάτω θα αναλύσουμε προβλήματα που βασίζονται στην ίδια αρχή με μεγαλύτερη όμως δυσκολία στον τρόπο που το κάθε στοιχείο συμβάλλει στο τελικό αποτέλεσμα

Θα βοηθήσει αρκετά, σε κάθε επανάληψη να θεωρούμε τον δείκτη και την τιμή που αναφέρεται ως **σταθερές** (**fixed**)

Για παράδειγμα, έστω ότι θέλουμε να υπολογίσουμε το άθροισμα κάποιων δυνάμεων του 2. Μας δίνεται λοιπόν ένας πίνακας με *n* αριθμούς, τους εκθέτες των δυνάμεων που θέλουμε να προσθέσουμε

$$[3, 2, 1, 2] \rightarrow 2^3 + 2^2 + 2^1 + 2^2 = 17$$

Όπως δουλέψαμε και σε προηγούμενα προβλήματα, θα χρειαστεί να διατρέξουμε τα στοιχεία του πίνακα

``` c++
for(int i = 0; i < n; i++){
    //Υπολόγισε 2 ^ a[i]
    //Πρόσθεσε το στο συνολικό αποτέλεσμα
}
```
Όσο υπολογίζουμε την τιμή $2^{a_i}$ δεν μας αφορά ότι η τιμή `a[i]` θα αλλάξει αργότερα, έτσι για να μην μπλεκόμαστε το αντιμετωπίζουμε σαν να ήταν σταθερά

Σε προηγούμενο κεφάλαιο, για να υπολογίζουμε την τιμή μίας βάσης `base` υψομένη σε κάποιον εκθέτη `expo` γράψαμε:

```c++
int ans = 1;
for(int i = 0; i < expo; i++)
    ans *= base;
```

Χρησιμοποιώντας την τιμή `a[i]` ως εκθέτη και αθροίζοντας τα αποτελέσματα σε μία μεταβλητή `sum` προκύπτει:

``` c++
int sum = 0;
for(int i = 0; i < n; i++){
    //Υπολόγισε 2 ^ a[i]
    int ans = 1;
    for(int j = 0; j < a[i]; j++)
        ans *= 2;
    //Πρόσθεσε το στο συνολικό αποτέλεσμα
    sum += ans;
}
```

Βλέπουμε ότι έχουμε ενσωματώσει τον έτοιμο κώδικα στο εξωτερικό `for` με τις εξής διαφορές:
- Αντικαταστήσαμε την μεταβλητή `expo` με το `a[i]`
- Αντικαταστήσαμε την μεταβλητή `base` με την τιμή 2, αφού η εκφώνηση μας ζητάει να υπολογίζουμε μόνο δυνάμεις του 2
- Μετονομάσαμε την μεταβλήτη που ορίζεται στο εσωτερικό `for` σε `j`, ώστε να μην υπάρχει σύγκρουση με την μεταβλητή `i` του εξωτερικού loop (θα δούλευε αν δεν αλλάζαμε όνομα? Αν ναι γιατί?)

---
## Πρόβλημα: [CSES/Repetitions](https://cses.fi/problemset/task/1069)

Μας δίνεται μία συμβολοσειρά χαρακτήρων που εκφράζει μία ακολουθία *DNA*. Η συμβολοσειρά περιέχει χαρακτήρες $A$, $C$, $G$ και $T$

Μας ζητείται να βρούμε το μέγεθος της μεγαλύτερης "επανάληψης" στην ακολουθία, δηλαδή το μέγεθος της μεγαλύτερης συνεχής υποσυμβολοσειράς που αποτελείται από τον ίδιο χαρακτήρα

$$ ATTC{\color{red}GGG}A \rightarrow 3 $$

### Λύση 1💡

Ας λύσουμε πρώτα ένα πίο απλό πρόβλημα

Για κάποιο συγκεκριμένο σημείο στη συμβολοσειρά, πόσο πίσω μπορώ να "επεκταθώ" ώστε όλα τα στοιχεία που επιλέγω να είναι ίδια? 

Π.χ Για την συμβολοσειρά *ATTAAAACT*:

- Για την θέση 0 $(A)$, δεν υπάρχει προηγούμενος χαρακτήρας ${\color{green}Α}TTAAAACT$
- Για την θέση 2 $(T)$, μέχρι και ο προηγούμενος χαρακτήρας είναι ίδιος
$A{\color{green}TT}AAAACT$
- Για την θέση 5 $(A)$, μέχρι και ο δευτερος προηγούμενος είναι ίδιος
$ATT{\color{green}AAA}ACT$

Αρκεί να βρίσκουμε αυτή την τιμή για κάθε θέση του πίνακα και να επιλέγουμε την μεγαλύτερη

```c++
string s = "ATTAAAACT";
int n = s.size(), ans = 0;
for(int i = 0; i < n; i++){
    //Δες πόσο πίσω μπορούμε να πάμε
    int j = i;
    while(j >= 0 && s[j] == s[i])
        j--;

    //Πόσους χαρακτήρες πήγαμε πίσω
    int count = i - j;
    
    //Αναναίωσε την μέγιστη εώς τώρα τιμή
    if(count > ans)
        ans = count;
}
```
> Γιατί δεν υπάρχει κίνδυνος η μεταβλητή j να έχει αρνητική τιμή όταν τον χρησιμοποιηούμε ως δείκτη του s?

### Λύση 2💡

Ας χωρίσουμε την συμβολοσειρά σε διαστήματα όπου όλα τα στοιχεία είναι ίδια

Ξεκινώντας από το δεύτερο στοιχείο, αν εκείνο διαφέρει από το προηγούμενο ξεκίνα καινούργιο διάστημα, αλλιώς, αν είναι ίδια, αύξησε το μέγεθος του πιο πρόσφατου διαστήματος 

$$A | TT | AAAA | C | T$$

Εφόσον μας ενδιαφέρει μόνο το μέγεθος του διαστήματος αρκεί να διατηρούμε σε μία μεταβλητή `int sz` το μέγεθος του τελευταίου διαστήματος

Μετά από κάθε στοιχείο που λαμβάνουμε υπόψιν, ελέγχουμε αν το διάστημα στο οποίο ανήκει είναι το μεγαλύτερο

``` c++
string s = "ATTAAAACT";
int n = s.size(), ans = 0;
//Το πρώτο στοιχείο ανοίκει στο πρώτο διάστημα
int sz = 1;

for(int i = 1; i < n; i++){
    if(a[i] == a[i-1]){
        //Αύξησε κατα 1 το μήκος του τελευταίου διάστηματος 
        sz++;
    }
    else{
        //Δημιούργησε ένα καινούργιο διάστημα στο οποίο ανήκει ο a[i]
        sz = 1;
    }
    //Αναναίωσε την μέγιστη εώς τώρα τιμή
    if(sz > ans)
        ans = sz;
}
```
### Χρήσιμες ιδέες 💭

- Είδαμε πώς μπορούμε να χωρίσουμε αποδοτικά έναν πίνακα σε διαστήματα ίδιων στοιχείων

### Προβληματισμοί 🔎

- Πώς μπορούμε να καταλήξουμε στην δεύτερη λύση μέσω της πρώτης?

- Ποιά από τις δύο λύσεις θεωρείτε ότι είναι καλύτερη και γιατί?

- Ποιά κριτήρια μπορούμε να χρησιμοποιήσουμε για να συγκρίνουμε δύο λύσεις?

## Πρόβλημα [κυλικείο](https://pdp-archive.github.io/27-PDP/a-xxx-statement) και [λύση](https://pdp-archive.github.io/27-PDP/a-xxx-solution)

## Επεξεργασία 2D πίνακα

Οι ιδέες που αναφέραμε για την γραμμική επεξεργασία μονοδιάστατων πινάκων μπορούν εύκολα να επεκταθούν για πολυδιάστατους πίνακες

Ο πιο απλός και συνήθης τρόπος να διατρέξουμε έναν 2D πίνακα $a$ με $n$ γραμμές και $m$ στήλες είναι να επεξεργαζόμαστε κάθε γραμμή $0,1,\dots, n-1$ ως έναν μονοδιάστο πίνακα του οποίου τα στοιχεία θα εξετάζουμε με την σειρά $0, 1, \dots, m-1$ 

Για παράδειγμα για να διαβάσουμε έναν 2D πίνακα:

```c++
for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++)
        cin >> a[i][j];
```
Για έναν πίνακα $4 \times 3$ τα στοιχεία της εισόδου τοποθετούνται στον πίνακα με τον εξής τρόπο (το στοιχείο $1$ αντιστοιχεί στο πρώτο στοιχείο της εισόδου)

```
| 1  | 2  | 3  |
| 4  | 5  | 6  |
| 7  | 8  | 9  |
| 10 | 11 | 12 |
```

Για 3D πίνακα διαστάσεων $n \times m \times k$ μπορούμε να επεξεργαζόμαστε κάθε επίπεδο $0, 1, \dots, n-1$. Έχοντας "παγώσει" ένα επίπεδο, μπορούμε να εφαρμόσουμε τον προαναφερόμενο αλγόριθμο για να διατρέξουμε τον $m \times k$ πίνακα στον οποίο αντιστοιχεί

### Πρόβλημα: [islandPerimeter](https://leetcode.com/problems/island-perimeter/description/)

Μας δίνεται ένας `n x m` πίνακας `grid` που αναπαριστά έναν χάρτη. Κάθε κελί του πίνακα μπορεί να είναι είτε 1 (γη) είτε 0 (νερό). Ένα κελί γης μπορεί να είναι συνδεδεμένο με άλλα κελιά γης οριζόντια ή κάθετα. Το σύνολο των κελιών γης ορίζει μοναδικό νησί. Μας ζητείται να υπολογίσουμε την περίμετρο του νησιού αυτού

![](island.png)

Το παραπάνω νησί έχει περίμετρο $16$

### Λύση:

Πόσο συμβάλλει κάθε κελί γης στο τελικό αποτέλεσμα?

Ένα κελί γης που περιβάλλεται από γη (όπως εκείνο στην θέση $(1, 1)$) δεν συνεισφέρει στην περίμετρο του νησιού, ένα κελί γης (όπως εκείνο στην θέση $(2, 1)$) που γειτνιάζει με $2$ κελιά θάλασσας συνεισφέρει $2$ μονάδες στην περίμετρο

Προκύπτει ότι ένα κελί γης $(i,j)$ που γειτνιάζει με $k$ άλλα κελιά γης συνεισφέρει $contr_{i,j}=4-k$ μονάδες στην περίμετρο

Μπορούμε να διατρέξουμε τον πίνακα, αν ένα στοιχείο $(i, j)$ που εξετάζουμε αντιστοιχεί σε κελί γης, θα υπολογίζουμε και θα προσθέτουμε στην περίμετρο την συνεισφορά του $contr_{i, j}$

``` c++
int perimeter = 0;
//διατρέχουμε τα στοιχεία του πίνακα
for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
        //ελέγχουμε ότι το κελί (i, j) είναι κελί γης
        if(grid[i][j] == 1){
            int contr = 4;
            //ελέγχουμε αν ο πάνω γείτονας είναι κελί γης 
            if(i-1 >= 0 && grid[i-1][j] == 1) contr--;
            //ελέγχουμε τον κάτω γείτονα
            if(i+1 < n && grid[i+1][j] == 1) contr--;
            //ελέγχουμε αριστερά
            if(j-1 >= 0 && grid[i][j-1] == 1) contr--;
            //ελέγχουμε δεξιά
            if(j+1 < m && grid[i][j+1] == 1) contr--;
            //προσθέτουμε την συνεισφορά του (i, j) στην περίμετρο
            perimeter += contr;
        }
    }
}
```

### Χρήσιμες ιδέες 💭

- Αναγνωρίζουμε τον τρόπο με τον οποίο κάθε κελί γης συμβάλλει στον υπολογισμό της περιμέτρου, η τεχνική αυτή είναι γνωστή ως **συνεισφορά στο άθροισμα / contribution to the sum**

- Χρησιμοποιήσαμε κατάλληλους περιορισμούς για να εξασφαλίσουμε ότι δεν βγαίνουμε εκτός του πίνακα όσο εξετάζουμε τα γειτονικά στοιχεία

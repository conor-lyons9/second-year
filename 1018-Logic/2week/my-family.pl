/* Rules */
child(X, Y) :- parent(Y, X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
mother(X, Y) :- female(X), parent(X, Y).
father(X, Y) :- male(X), parent(X, Y).
/* Doesn't have "different" */
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y).
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y).

/* lab1 task */
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).

sibling(X, Y) :- brother(X, Y); sister(X, Y).
cousin(X, Y) :- parent(Z, X), parent(A, Y), sibling(Z, A).

/* People */
female(pam).
female(liz).
female(mary).
female(ann).
male(tom).
male(bob).
male(jim).
male(ciaran).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, mary).
parent(mary, jim).
parent(tom, ciaran).
parent(ciaran, goblin).

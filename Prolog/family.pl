
parent(john, ann). %the fact that John is a parent of Ann
parent(john, mike). %the fact that John is a parent of Mike
parent(mary, mike).
parent(mike, pat).
parent(mike, bob).
parent(pat, ben).
female(mary). %the fact that Mary is a female
female(ann).
female(pat).
male(john). %the fact that John is a male
male(mike).
male(bob).
male(ben).
mother(X,Y) :- parent(X, Y), female(X).
father(X,Y) :- parent(X, Y), male(X).
grandparent(X,Z):- parent(X,Y),parent(Y,Z).
sister(X,Y):- parent(Z,X), parent(Z,Y),female(X).

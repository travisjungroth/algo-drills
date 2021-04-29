# Algo Drills

A command line tool for memorizing algorithms in Python by typing them. In alpha and things will change.

## How it works

1. Type out an algorithm based on its function signature and docstring.
2. See what you did wrong or get a new algorithm.
3. Repeat until bored.

## Getting Started

1. [Clone this repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
   .
2. Look at `algorithms/bisect_search.py` and its references.
3. Run `./drill.py practice`
4. Fill out the newly created `worskpace.py` to match the code in `algorithms/bisect_search.py`. Do it from memory or look back at
   the file.
5. Run `./drill.py practice` again. You'll do this a lot. Maybe make a shortcut.
6. If your code matches, it will be deleted and you can try again. If it's different, you'll get a diff.
7. Check out other algorithms that look interesting in `algorithms/`.
8. If you see an algorithm you like, copy-paste its ID to `user_data/allowed.csv`.
9. Run `./drill.py -h` to see more features.
10. Keep going!

## FAQ

#### Isn't memorizing bad?

No. Memorization without understanding is bad. You should understand an algorithm well before committing it to memory.

#### Are these the best versions of these algorithms?

No. They're versions the author likes.

#### Can I view my history?

Yes! Check out `user_data/history.txt` for a nice format. Maybe keep it open in a window for motivation.

#### Can I add my own algorithms?

Yes! `./drills.py new_algo --help`

#### Can I see all the algorithms for a specific reference?

Yes! Just two books right now. `./drills.py reference --help`

#### Can I help?

Yes! Tell me how you like this tool, submit a bug report (or fix!), tell me if you have a feature idea, show your
friends, or show me your own cool algorithms. You can email me at my last name at gmail, or message me on reddit
at [/u/travisjungroth](https://www.reddit.com/u/travisjungroth).

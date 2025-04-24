# molecular_genetics_research_project
 Final project for BI4110

## Brainstorming
### Bacterial transformation
Create a simulation of the pGLO transformation lab. This would include a simulated cell, simulated DNA, and simulated protein synthesis. Potential issues include learning how to do dynamic animations (cell wall and soft-body animations), appropriately using object-oriented design, and ensuring that there are no fatal errors in the program.

---
### Genetic repair
A simulated demonstration of genetic repair. This would contain different simulated proteins, but I really think they would just be coded to have the function that they exhibit as opposed to coding the individual amino acids and letting the simulation figure out what to do.

---
### DNA sequencing virtual lab
Simulate some DNA. Code different sequencing methods (kind of like a level-based game) that use first gen, next gen, and nanopore sequencing

---
## Addons
### Color Coding
Let nucleotides and/or amino acids be color-coded. This would make use of escape characters (in c++ and python, the languages for this project: `"\x1b[38;2;RED;GREEN;BLUEmTEXT GOES HERE\x1b[0m"`)

### Command line
Perform C++ usage and/or custom command line prompts. Most of these look like they will use the pgzero package, but I am tempted to let the user configure certain settings using a custom command line. Syntax would be `[object].[setting] [action] [argument(s)]`

So a command to change the color of amino acid LEU to rgb 100, 100, 100 would look like this:

`LEU.color set 100 100 100`

And to increase the red color of base pair T by 50 (Args not provided are assumed to be zero):

`base_T.color increase 50`

Or to change the output format to a string

`output.format set STR`
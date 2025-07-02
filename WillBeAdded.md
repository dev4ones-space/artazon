# Will be added to app

**App managment** (as menu, will be added at 11??: 1.1):

- List packages (apps too, as another option)
- Install apps (will be some pre-included apps for rooting and other)
- Remove apps

**Root managment** (as menu, not planned for adding now):

- Install root (as another menu)
- Check root
- Install some modules (pre-included modules)

**Mispell in code** (very dumb, but to make it more understandable)

if CurrentOS not in main.SupportedPlatoforms: main.activities.UnsupportedOS()
                                      ^
Also in main:

class main:
    ...
    SupportedPlatoforms = ['Darwin', 'Linux']
                 ^

# Python plugins for juCi++

## Requirements

* `python>=3.5`
* `pygobject-3.0`

Also you need the python package gi-introspection

## How plugins work
#### Loading

Plugins resided in the plugin directory will be loaded automatically.
#### Init

Plugins will not initialize unless explicitly told in the plugin-file.
Usually with a call to a init function at the bottom of the file.
#### Menu elements and keybindings to actions

Read the gtk documentation and see examples in the snippet and tools plugins in this
repo.
#### Programming python in juCi++

JuCi++ will parse and try to reload the plugin on every save while working in the
plugin-directory.
#### Developing outside of juCi++
The module jucipp which contains the api is only available to python if loaded through
juCi++. This is because the api is an internal type of the juCi++ executable.

#### Configuration

The plugin feature has two options in config.json to configure various paths
```json
"python": {
    "site_packages": "<path>",
    "plugin_directory": "<path>"
}
```

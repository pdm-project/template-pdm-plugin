# pdm-plugin

> A template for PDM plugin project

## Installation

You can either install the plugin globally or in your project.

Enable the plugin globally:

```
pdm self add pdm-plugin
```

Or, enable the plugin in your project:

```toml
[tool.pdm]
plugins = ["pdm-plugin"]
```
And run the following command once in your project:

```
pdm install --plugins
```

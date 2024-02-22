# pdm-plugin

> A template for PDM plugin project

## Installation

Enable the plugin:

```
pdm self add pdm-plugin
```

Enable the plugin in your project:

```toml
[tool.pdm]
plugins = ["pdm-plugin"]
```
And run the following command once in your project:

```
pdm install --plugins
```

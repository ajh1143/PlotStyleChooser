# Plot Style Detective

### Function

Discover which plotting style you prefer, by generating a sample of each of the 23 most popular styles in MatPlotLib, either using a compatible dictionary-based dataset, or by using the default data example. 

### Plot Styles Included:
```
'bmh', 'seaborn-poster', 'seaborn-darkgrid', 'seaborn-paper', 'classic', 'seaborn', 'grayscale' 

'seaborn-dark', 'seaborn-talk', 'seaborn-dark-palette', 'seaborn-colorblind', 'seaborn-bright' 

'seaborn-ticks', 'seaborn-muted', 'seaborn-pastel', 'seaborn-notebook', '_classic_test', 'fivethirtyeight' 

'seaborn-white', 'seaborn-whitegrid', 'seaborn-deep', 'dark_background', 'ggplot'
```

#### Imports
```Python3
import matplotlib.pyplot as plt
```

#### Class
```Python3
class PlotChoices()
```

#### Find Available Styles
```Python3
    def PlotStyles(self):
    """
    Generates amd returns a list of the top 23 styles native to MatPlotLib
    """
        styles = plt.style.available
        return styles
```

#### Generate Plots
```Python3

    def barPlots(self, dict_data, types):
    """
    Function: Uses dictionary dataset to create 23 different bar plots with different 
               styles selected
    
    Args: dict_data: your datase, expected to be in dictionary format
          types: List of style names to use for each plot generated
          
    Note: define the dict_data parameter as 'default' to use a pre-set dataset
    """
    
        #Test if user entered 'default' as data_dict to use pre-built dataset
        if dict_data == 'default':
            dict_data = {'Group A': 25, 'Group B': 50, 'Group C': 75}
        #If using a novel dictionary dataset appropriate for a bar plot, use as 'dict_data'
        else:
            dict_data = dict_data
        names = list(dict_data.keys())
        values = list(dict_data.values())
        for each in types:
            plt.style.use(each)
            plt.bar(range(len(dict_data)), values, tick_label=names)
            plt.title('Style = ' + each)
            plt.xlabel('X-Axis Label')
            plt.ylabel('Y-Axis Label')
            plt.tight_layout()
            plt.show()
```

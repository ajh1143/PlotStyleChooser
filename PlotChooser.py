import matplotlib.pyplot as plt


class PlotChoices():

    def PlotStyles(self):
    """
    Generates amd returns a list of the top 21 styles native to MatPlotLib
    """
        styles = plt.style.available
        return styles

    
    def barPlots(self, dict_data, types):
    """
    Function: Uses dictionary dataset to create 21 different bar plots with different styles selected
    
    Args: dict_data: your datase, expected to be in dictionary format
          types: List of style names to use for each plot generated
    """
    
        for each in types:
            plt.style.use(each)
            names = list(dict_data.keys())
            values = list(dict_data.values())
            plt.bar(range(len(dict_data)), values, tick_label=names)
            plt.title('Style = '+each)
            plt.xlabel('X-Axis Label')
            plt.ylabel('Y-Axis Label')
            plt.tight_layout()
            plt.show()


if __name__ == "__main__":

  data = {'Group A':25, 'Group B': 75, 'Group C':50}
  run = PlotChoices()
  style = run.PlotStyles()
  run.barPlots(data, style)

from __future__ import print_function
import pandas as pd

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# data exploration widgets

def generate_widget(df):

    def f(viz = 'X-Y', colx = '', coly = '', colz = '', colw = 10, na = False, asc = '', source = df):
        if(viz == 'X-Y'):
            temp = source
            if na:
                temp = temp.fillna(-1000)
            trace = go.Scattergl(
                x = temp[colx],
                y = temp[coly],
                name = coly + ' vs ' + colx,
                mode = colz
            )
            layout = go.Layout(
                title=coly + ' vs ' + colx,
                yaxis=dict(
                    title=coly
                ),
                xaxis=dict(
                    title=colx
                )
            )
            
        elif(viz == 'pareto'):
            sort_order = (asc == 'Ascending')
            temp = source
            if na:
                temp = temp.fillna(-1000)
            grouped = temp.groupby(colx)
            
            if(coly in ['count', 'sum', 'mean', 'std', 'max', 'min']):
                grouped = grouped.agg(
                    {
                        colz : [coly]
                    }
                )
            elif(coly == 'uniques'):
                grouped = grouped.apply(
                    lambda g: pd.Series(g[colz].unique().size, index = pd.MultiIndex.from_product([[colz],[coly]]))
                )
                

            
            grouped = grouped.reset_index().sort_values([(colz, coly)], ascending=sort_order).head(colw)\
                .sort_values([(colz, coly)], ascending = (not sort_order))

#             print(grouped)

            trace = go.Bar(
                y=grouped[colx],
                x=grouped[colz][coly],
                name=colx,
                marker=dict(
                    color='rgb(49,130,189)'
                ),
                orientation = 'h'
            )
            layout = go.Layout(
                title=coly + ' of ' + colz + ' by ' + colx,
                yaxis=dict(
                    title=colx,
                    type = "category",
#                     categoryorder = "category descending"
                    tickformat =".3f"
                ),
                xaxis=dict(
                    title=coly + ' of ' + colz
                ),
                margin=dict(
                    l = 160
                )
            )

        else:
            temp = source
            if na:
                temp = temp.fillna(-1000)
            trace = go.Histogram(x=temp[colx],
                            name=colx,
                            marker=dict(
                                color='rgb(49,130,189)')
                        )
            layout = go.Layout(
                title='distribution',
                yaxis=dict(
                    title='count'
                ),
                xaxis=dict(
                    title=colx
                )
            )
            
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.iplot(fig)
    
    cols = df.columns
    viz = widgets.Dropdown(options = ['pareto', 'distribution', 'X-Y'])
    col1 = widgets.Dropdown(options = cols)
    col2 = widgets.Dropdown(options = ['count', 'sum', 'mean', 'std', 'max', 'min', 'uniques'])
    col3 = widgets.Dropdown(options = [c for c in cols if c != col1.value], disabled = False)
    col4 = widgets.Dropdown(options = [10,20,50,100], disabled = False)
    null_inclusion = widgets.Checkbox(
                        value=False,
                        description='Fill NA with -1000',
                    )
    asc_desc = widgets.Dropdown(options = ['Descending', 'Ascending'], disabled = False)
    
    def update_cols(change):
        if(change['new'] == 'pareto'):
            col2.options = ['count', 'sum', 'mean', 'std', 'max', 'min', 'uniques']
            col2.disabled = False
            col3.options = [c for c in cols if c != col1.value]
            col3.disabled = False
            col4.disabled = False
            asc_desc.disable = False
        elif(change['new'] == 'distribution'):
            col2.options = ['']
            col2.disabled = True
            col3.options = ['']
            col3.disabled = True
            col4.disabled = True
            asc_desc.disable = True
        elif(change['new'] == 'X-Y'):
            col2.options = cols
            col2.disabled = False
            col3.options = ['lines', 'markers', 'lines+markers']
            col3.disabled = False
            col4.disabled = True
            asc_desc.disable = True
    
    def update_col3(change):
        col3.options = [c for c in cols if c != col1.value]
    
    viz.observe(update_cols, 'value')
    col1.observe(update_col3, 'value')
    
    ui = widgets.VBox(
        [widgets.HBox([viz, null_inclusion, widgets.Label('(Pandas ignores NA/Null by default)')])
         , widgets.HBox([col1, col2, col3, col4, asc_desc])]
    )
    out = widgets.interactive_output(f
                                     , {'viz': viz
                                        , 'colx': col1
                                        , 'coly': col2
                                        , 'colz': col3
                                        , 'colw': col4
                                        , 'na' : null_inclusion
                                        , 'asc' : asc_desc})
    display(ui, out)
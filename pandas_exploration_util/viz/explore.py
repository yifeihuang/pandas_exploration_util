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

def xy(colx, agg, colz, hover_display, source, mode = 'markers'):
    # colx : x axis, str
    # colz : y axis, str
    # coly : aggregation function to apply to colz, str {'unaggregated' 'count', 'sum', 'mean', 'std', 'max', 'min'}
    # hover_display: column to display for hover, only for unaggregated, str
    # source: dataframe
    # for a point and click version of this check out: https://github.com/yifeihuang/pandas_exploration_util
    print(
        '{}: {:0.1%} null ({:d} out of {:d})'\
            .format(
                colx
                , source[colx].isnull().sum() / source.shape[0]
                , source[colx].isnull().sum()
                , source.shape[0]
            )
        )
    print(
        '{}: {:0.1%} null ({:d} out of {:d})'\
            .format(
                colz
                , source[colz].isnull().sum() / source.shape[0]
                , source[colz].isnull().sum()
                , source.shape[0]
            )
        )
    
    data = []
    for i in range(len(agg)):
        temp = source
        if(agg[i] == 'unaggregated'):
            grouped = temp.loc[:, [colx, colz]].set_index(colx)
            grouped.columns = pd.MultiIndex.from_product([[colz],[agg[i]]])
        if(agg[i] in ['count', 'sum', 'mean', 'std', 'max', 'min', 'median']):
            grouped = temp.groupby(colx).agg(
                {
                    colz : [agg[i]]
                }
            )
        elif(agg[i] == 'uniques'):
            grouped = temp.groupby(colx).apply(
                lambda g: pd.Series(g[colz].unique().size, index = pd.MultiIndex.from_product([[colz],[agg[i]]]))
            )
        # print(grouped.head())

        if(agg[i] == 'unaggregated'):
            trace = go.Scattergl(
                x = grouped.index,
                y = grouped[colz][agg[i]],
                name = agg[i] + ' of ' + colz + ' vs ' + colx,
                mode = mode[i],
                text = source[hover_display],
                hoverinfo = 'text'
            )

        else:
            trace = go.Scattergl(
                x = grouped.index,
                y = grouped[colz][agg[i]],
                name = agg[i] + ' of ' + colz + ' vs ' + colx,
                mode = mode[i]
            )
        data.append(trace)
        
    layout = go.Layout(
        title=(', ').join(agg) + ' of ' + colz + ' vs ' + colx,
        yaxis=dict(
            title=colz
        ),
        xaxis=dict(
            title=colx
        )
    )
    
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig)
    
def distribution(colx, source):
    print(
        '{}: {:0.1%} null ({:d} out of {:d})'\
            .format(
                colx
                , source[colx].isnull().sum() / source.shape[0]
                , source[colx].isnull().sum()
                , source.shape[0]
            )
        )
    temp = source

    if coly == 'Absolute Unit':
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
    else:
        trace = go.Histogram(x=temp[colx],
                        name=colx,
                        histnorm='percent',
                        marker=dict(
                            color='rgb(49,130,189)')
                    )
        layout = go.Layout(
            title='distribution',
            yaxis=dict(
                title='Percent (%)'
            ),
            xaxis=dict(
                title=colx
            )
        )

    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig)



def generate_widget(df):

    def f(viz = 'X-Y', colx = '', coly = '', colz = '', colw = 10, na = False, asc = '', source = df):
        if(viz == 'X-Y'):
            print(
                '{}: {:0.1%} null ({:d} out of {:d})'\
                    .format(
                        colx
                        , source[colx].isnull().sum() / source.shape[0]
                        , source[colx].isnull().sum()
                        , source.shape[0]
                    )
                )
            print(
                '{}: {:0.1%} null ({:d} out of {:d})'\
                    .format(
                        colz
                        , source[colz].isnull().sum() / source.shape[0]
                        , source[colz].isnull().sum()
                        , source.shape[0]
                    )
                )

            temp = source
            if na:
                temp = temp.fillna(-1000)
            
            
            if(coly == 'unaggregated'):
                grouped = temp.loc[:, [colx, colz]].set_index(colx)
                grouped.columns = pd.MultiIndex.from_product([[colz],[coly]])
            if(coly in ['count', 'sum', 'mean', 'std', 'max', 'min']):
                grouped = temp.groupby(colx).agg(
                    {
                        colz : [coly]
                    }
                )
            elif(coly == 'uniques'):
                grouped = temp.groupby(colx).apply(
                    lambda g: pd.Series(g[colz].unique().size, index = pd.MultiIndex.from_product([[colz],[coly]]))
                )
            # print(grouped.head())

            trace = go.Scattergl(
                x = grouped.index,
                y = grouped[colz][coly],
                name = coly + ' of ' + colz + ' vs ' + colx,
                mode = colw
            )
            layout = go.Layout(
                title=coly + ' of ' + colz + ' vs ' + colx,
                yaxis=dict(
                    title=coly + ' of ' + colz
                ),
                xaxis=dict(
                    title=colx
                )
            )
            
        elif(viz == 'pareto'):
            print(
                '{}: {:0.1%} null ({:d} out of {:d})'\
                    .format(
                        colx
                        , source[colx].isnull().sum() / source.shape[0]
                        , source[colx].isnull().sum()
                        , source.shape[0]
                    )
                )
            print(
                '{}: {:0.1%} null ({:d} out of {:d})'\
                    .format(
                        colz
                        , source[colz].isnull().sum() / source.shape[0]
                        , source[colz].isnull().sum()
                        , source.shape[0]
                    )
                )
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

        elif(viz == 'distribution'):
            print(
                '{}: {:0.1%} null ({:d} out of {:d})'\
                    .format(
                        colx
                        , source[colx].isnull().sum() / source.shape[0]
                        , source[colx].isnull().sum()
                        , source.shape[0]
                    )
                )
            temp = source
            if na:
                temp = temp.fillna(-1000)
            
            if coly == 'Absolute Unit':
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
            else:
                trace = go.Histogram(x=temp[colx],
                                name=colx,
                                histnorm='percent',
                                marker=dict(
                                    color='rgb(49,130,189)')
                            )
                layout = go.Layout(
                    title='distribution',
                    yaxis=dict(
                        title='Percent (%)'
                    ),
                    xaxis=dict(
                        title=colx
                    )
                )
            
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.iplot(fig)
    
    cols = df.columns

    desc_style = {'description_width': 'initial'}

    viz = widgets.Dropdown(options = ['pareto', 'distribution', 'X-Y'], description = "Choose Visualization", style = desc_style)
    col1 = widgets.Dropdown(options = cols, description = "Group By", style = desc_style)
    col2 = widgets.Dropdown(options = ['count', 'sum', 'mean', 'std', 'max', 'min', 'uniques']
                            , description = "Calculate", style = desc_style)
    col3 = widgets.Dropdown(options = [c for c in cols if c != col1.value], disabled = False
                            , description = " of ", style = desc_style)
    col4 = widgets.Dropdown(options = [10,20,50,100], disabled = False
                            , description = "Show Top ", style = desc_style)
    null_inclusion = widgets.Checkbox(
                        value=False,
                        description = "Fill NA with -1000 (Pandas ignores NA/Null by default)", 
                        style = desc_style
                    )
    asc_desc = widgets.Dropdown(options = ['Descending', 'Ascending'], disabled = False)
    
    def update_cols(change):
        if(change['new'] == 'pareto'):
            col1.description = 'Group By'
            col2.description = 'Calculate'
            col3.description = ' of '
            col4.description = 'Show Top '
            col2.options = ['count', 'sum', 'mean', 'std', 'max', 'min', 'uniques']
            col2.disabled = False
            old_val = col3.value
            col3.options = [c for c in cols if c != col1.value]
            col3.value = old_val
            col3.disabled = False
            col4.options = [10,20,50,100]
            col4.disabled = False
            asc_desc.disabled = False
        elif(change['new'] == 'distribution'):
            col1.description = 'Plot Distribution of '
            col2.description = 'In '
            col3.description = ''
            col4.description = ''
            col2.options = ['Absolute Unit', 'Percent']
            col2.disabled = False
            col3.options = ['']
            col3.disabled = True
            col4.disabled = True
            asc_desc.disabled = True
        elif(change['new'] == 'X-Y'):
            col1.description = 'Plot '
            col2.description = 'Vs '
            col3.description = 'Of '
            col4.description = 'Using '
            col2.options = ['unaggregated', 'count', 'sum', 'mean', 'std', 'max', 'min', 'uniques']
            col2.disabled = False
            old_val = col3.value
            col3.options = [c for c in cols if c != col1.value]
            col3.value = old_val
            col4.options = ['markers', 'lines', 'lines+markers']
            col3.disabled = False
            col4.disabled = False
            asc_desc.disabled = True
    
    def update_col3(change):
        if (viz.value in ['pareto', 'X-Y']) and col1.value == col3.value:
            col3.options = [c for c in cols if c != col1.value]
        else:
            pass
    
    viz.observe(update_cols, 'value')
    col1.observe(update_col3, 'value')

    ui = widgets.VBox(
        [
            widgets.HBox([
                viz
                , null_inclusion
            ])
            , widgets.HBox([col1])
            , widgets.HBox([col2, col3])
            , widgets.HBox([col4, asc_desc])]
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
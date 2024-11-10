import plotly.express as px
import plotly.graph_objects as go

def getAvgConcentrationByDate(df, column):
    tempdf = df[[column,"Date"]]
    tempdf = tempdf.groupby(["Date"]).mean().sort_values(by="Date")
    return tempdf

def plotTimeSeries(df, columns):
    fig = go.Figure()
    for column in columns:
        tempdf = getAvgConcentrationByDate(df, column)
        fig.add_trace(
            go.Scatter(
                x = tempdf.index,
                y = tempdf[column],
                mode = 'lines',
                name = f'{column} Concentration'
                )
            )
        fig.update_layout(
            title = 'Time Series of Air Quality Pollutants',
            xaxis_title = 'Date', yaxis_title='Concentration'
            )
    return fig

def plotCorrelationHeatmap(df, columns):
    corr_matrix = df[columns].corr()
    fig = px.imshow(
        corr_matrix,
        text_auto = True,
        color_continuous_scale = 'bluered',
        title = 'Correlation Heatmap of Air Quality Measurements'
        )
    return fig

def plotHistogram(df, column):
    fig = px.histogram(
        df,
        x = column,
        nbins = 60,
        histnorm = '',
        title = f'Histogram of {column} Concentration',
        labels = {
            f'{column}': f'{column} Concentration'
            }
        )
    return fig

def plotBoxplot(df, y):
    df['Month'] = df.index.month
    fig = px.box(
        df,
        x = 'Month',
        y = y,
        title = f'Monthly Distribution of {y} Concentration',
        labels = {
            'Month': 'Month',
            f'{y}': f'{y} Concentration'
            }
        )
    return fig

def plotScatterplot(df, x, y):
    fig = px.scatter(
        df,
        x = x,
        y = y,
        title = f'Scatter Plot of {y} Concentration vs {x}',
        labels = {
            f'{x}': f'{x} {"(°C)" if x=="Temperature" else ""}',
            f'{y}': f'{y} Concentration'}
        )
    return fig

def plotStackedAreaChart(df, columns):
    daily_avg = df.groupby('Date')[columns].mean()
    fig = px.area(
        daily_avg,
        x = daily_avg.index,
        y = daily_avg.columns,
        title = 'Stacked Area Chart of Daily Average Pollutant Levels',
        labels = {
            'value': 'Average Concentration',
            'Day': 'Date'}
        )
    return fig
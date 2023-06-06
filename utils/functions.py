import pandas as pd

def clean_data(df):
    dff = df.loc[~((df['poutcome'] == 'nonexistent') & (df['y'] =="yes"))]
    dff = dff.drop_duplicates()
    dff = dff[dff.marital != "unknown"]
    primer_quantil = dff['campaign'].quantile(.25) # Se toma el valor del primer cuantil
    tercer_quantil = dff['campaign'].quantile(.75) # Se toma el valor del tercer cuantil
    diff = tercer_quantil - primer_quantil # se establece la diferencia para determinar el piso y el techo, es decir todo lo que sea n veces superior o inferior
    piso = primer_quantil - 1.5 * diff
    techo = tercer_quantil + 1.5 * diff
    dff = dff[dff['campaign'] >= piso] # se filtran outliers inferiores
    dff= dff[dff['campaign'] <= techo] # se filtran outliers superiores
    return dff

def cohorte_numericas(dff, column):
    
    quantil = dff[column].quantile(0)
    primer_quantil = dff[column].quantile(.20) # Se toma el valor del primer cuantil
    segundo_quantil = dff[column].quantile(.40)
    tercer_quantil = dff[column].quantile(.60)
    cuarto_quantil = dff[column].quantile(.80)
    quinto_quantil = dff[column].quantile(1)
    quantiles = [quantil,primer_quantil,segundo_quantil,tercer_quantil,cuarto_quantil, quinto_quantil]
    grp_dff = dff.groupby([pd.cut(dff[column], quantiles), "y"])[["y"]].count()
    grp_dff  = grp_dff.rename(columns = {"y":"Total"}).reset_index()

    return grp_dff
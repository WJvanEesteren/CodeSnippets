for source in source_list:
        try:
            dfSource = getattr(ds, source)
            #print(dfSource.dtypes)
            if source == 'dfOECD':
                dfSource['date'] = dfSource["date"].dt.strftime("%Y-%M-%d")
                dfSource['date'] = pd.to_datetime(dfSource['date'], format='%Y-%m-%d')
                dfSource.dtypes
                print(dfSource['date'])
                exit()
            else:
                dfSource['date'] = pd.to_datetime(dfSource['date'], format='%Y-%m-%d')
            #print(dfSource.dtypes)
            index_list = ['country', 'date']
            dfSource = dfSource.set_index(index_list)
            dfData = dfData.join(dfSource)
            #dfSource.to_csv(source + '.csv', sep=';')
            print('Succesfully added {} to fact table.'.format(source))
        except Exception as e:
            print('Could not add {} to fact table: {}'.format(source, e))
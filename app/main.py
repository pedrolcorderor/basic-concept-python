#cada archivo de python de manera implicita es un modulo , pero lo haremos de manera explicita para que cumpla ciertas tareas en este caso el de las utilidades
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  print(data)
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  

if __name__ == '__main__':
  run()
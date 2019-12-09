require 'yaml'
require 'csv'

x = YAML.load_file('SkyTeam-Exchange.yaml')
start_date  = Date.new(2017, 01, 01)
end_date  = Date.new(2018, 01, 01)
date_list = (start_date .. end_date).map{ |day| day.strftime("%Y-%m-%d") }

CSV.open("TEST.csv", "w", {col_sep: ";"}) do |csv|
  csv << ['Date', 'Flight', 'From', 'Status', 'To', 'FF(ticket number?)', 'Class', 'Fare']
  date_list.each do |date|
    if x[date]
    x[date].each do |key, value|
      value["FF"].each do |k, v|
        a = [date, key, value["FROM"],value["STATUS"], value["TO"], k, v["CLASS"], v["FARE"]]
        csv << a
      end
    end
    end
  end
end

require 'csv'

desc "Import data from csv file"
task :import => [:environment] do

  file = "db/data.csv"

  CSV.foreach(file, :headers => true) do |row|
    Team.create {
      :name => row[1],
      :league => row[2],
      :some_other_data => row[4]
    }
  end

end

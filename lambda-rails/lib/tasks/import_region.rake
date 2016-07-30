#lib/tasks/import.rake
require 'csv'
desc "Imports a CSV file into an ActiveRecord table"
task :import, [:filename] => :environment do
  CSV.foreach('db/regions.csv', :headers => true, :row_sep => "\r\n", :quote_char => "\x00") do |row|
    Region.create!(row.to_hash)
  end
end

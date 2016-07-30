class CreateRegions < ActiveRecord::Migration
  def change
    create_table :regions do |t|
      t.integer :postcode
      t.integer :region_code
      t.text :state
      t.text :region_name

      t.timestamps null: false
    end
  end
end

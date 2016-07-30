class ModifyUser < ActiveRecord::Migration
  def change
    add_column :users, :is_male, 		:boolean
    add_column :users, :occ_code, 		:integer
    add_column :users, :has_partner, 	:boolean
    add_column :users, :region, 		:integer
    add_column :users, :used_tax_agent, :boolean
    add_column :users, :salary_wages, 	:decimal
    remove_column :users, :name
  end
end

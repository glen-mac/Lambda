class HomeController < ApplicationController

  def index
    # conn = Faraday.new(:url => 'https://rubygems.org') do |faraday|
    #   faraday.request  :url_encoded             # form-encode POST params
    #   faraday.response :logger                  # log requests to STDOUT
    #   faraday.adapter  Faraday.default_adapter  # make requests with Net::HTTP
    # end
    # response = conn.get '/api/v1/versions/httparty.json'
    # response.body
    # render json: response.body

  end


end

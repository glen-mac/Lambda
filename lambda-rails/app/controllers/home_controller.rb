class HomeController < ApplicationController

  require "json"

  def getData
    conn = Faraday.new(:url => 'https://api.twitter.com') do |faraday|
      faraday.request  :url_encoded             # form-encode POST params
      faraday.response :logger                  # log requests to STDOUT
      faraday.adapter  Faraday.default_adapter  # make requests with Net::HTTP
    end

    # ## POST ##
    # post payload as JSON instead of "www-form-urlencoded" encoding:
    response = conn.post do |req|
      req.url '/nigiri'
      req.headers['Content-Type'] = 'application/json'
      req.body = '{ "isMale": #{params["gender"]},
                    "ageRange": #{params["age_range"]},
                    "occupationCode": #{params["occupation"]},
                    "maritalStatus": #{params["marital_status"]},
                    "regionCode": #{params["region"]},
                    "taxAgent": #{params["tax_agent"]},
                    "salaryWages": #{params["sw_amount"]}}'
    end

    # response = conn.get '/1.1/statuses/user_timeline.json'
    parsed = JSON.parse(response.body) # returns a hash

    #parsed["errors"][0]["code"]
    #params["email"]

    # @user = User.new
  end

  def index
  end

  def submit
    #redirect_to root_path and return if params[:spam].present?
    # @user = Contact.new(contact_params)
    # if @user.valid?
    #   #ContactFormMailer.admin(@contact).deliver
    #   #redirect_to root_url
    #   #flash[:success] = "Message sent! Thank you for contacting us"
    # else
    render json: getData()
    flash[:error] = "There was an error in your submission."
    #end
  end


end

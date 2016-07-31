class HomeController < ApplicationController

  require "json"

  def getData
    conn = Faraday.new(:url => 'http://10.1.3.225:8080') do |faraday|
      faraday.request  :url_encoded             # form-encode POST params
      faraday.response :logger                  # log requests to STDOUT
      faraday.adapter  Faraday.default_adapter  # make requests with Net::HTTP
    end

    # ## POST ##
    # post payload as JSON instead of "www-form-urlencoded" encoding:

    region = Region.find_by_postcode(params["region"])

    if(region == nil)
      return false
    end

    regionCode = region.region_code

    res = conn.post do |req|
      req.url '/process'
      req.headers['Content-Type'] = 'application/json'
      req.body = %Q({ "isMale": #{params["gender"]},
                      "ageRange": #{params["age_range"]},
                      "occupationCode": #{params["occupation"]},
                      "maritalStatus": #{params["marital_status"]},
                      "regionCode": #{regionCode},
                      "taxAgent": #{params["tax_agent"]},
                      "salaryWages": #{params["sw_amount"]}})
                      end

                      res.body # returns a hash

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
                        #
                        if(params["sw_amount"].to_f <= 0)
                          flash[:error] = "Salary and Wages cannot be 0"
                          render "index"
                          return
                          # elsif(params["postCode"].to_i == 0)
                          #   flash[:error] = "Postcode must be entered."
                          #   render "index"
                          #   return
                        end

                        result = getData()
                        if (result != false)
                          @new = "hey!!"
                          render "result" #{}"result"
                        else
                          flash[:error] = "The Postcode entered could not be found."
                          render "index"
                        end
                        #end
                      end


                      end

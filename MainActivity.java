package com.example.workforliving;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.HttpResponse;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import static android.util.Log.d;

public class MainActivity extends AppCompatActivity {

    static String jobTitleInput;
    static String locationInput;
    static String selection;
    static String zipcode;
    static String jobTitle;
    static int count;
    static String salary;
    static String companyName;
    static String address;
    static String price;
    private RequestQueue mQueue;

    @Override
    protected void onCreate(final Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        jobTitleInput = findViewById(R.id.jobTitle).toString();
        locationInput = findViewById(R.id.Location).toString();
        RadioGroup rg1 = findViewById(R.id.homeType);
        if(rg1.getCheckedRadioButtonId()!= -1){
            int id= rg1.getCheckedRadioButtonId();
            View radioButton = rg1.findViewById(id);
            int radioId = rg1.indexOfChild(radioButton);
            RadioButton btn = (RadioButton) rg1.getChildAt(radioId);
            selection = (String) btn.getText();
        }

        mQueue = Volley.newRequestQueue(this);
        //final String url = "http://47.110.241.234:8000/api/atlantaJobQuery?infos={%22index%22:%220%22,%20%22zipcode%22:%2230313%22,%20%22hometype%22:%22apartment%22,%20%22title%22:%22Developer%22}";
        String url = "http://47.110.241.234:8000/api/atlantaJobQuery?infos={\"index\":" + "\"" + count + "\"" + "," + " \"zipcode\":" + "\"" + locationInput + "\"" +  "," +" \"hometype\":" + "\"" +selection + "\"" + ", \"title\":" + "\"" + jobTitleInput + "\"" + "}" ;
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse (JSONObject response) {
                        JSONArray array = new JSONArray();
                        try {
                            JSONObject job = array.getJSONObject(0);
                            JSONObject house = array.getJSONObject(1);
                            zipcode = job.getString("zipcode");
                            jobTitle = job.getString("title");
                            companyName = job.getString("employer");
                            address = house.getString("location");
                            price = house.getString("price");
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            public void onErrorResponse (VolleyError error) {
                error.printStackTrace();
            }
        });
        mQueue.add(request);


        View button = (Button) findViewById(R.id.matchButton);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent newIntent = new Intent (MainActivity.this, resultPage.class);
                startActivity(newIntent);
            }
        });
    }




}
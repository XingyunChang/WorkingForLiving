package com.example.myapplication;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;


public class resultPage extends AppCompatActivity {
    private TextView companyNameResult;
    private TextView positionNameResult;
    private TextView salaryResult;
    private TextView addressResult;
    private TextView housePriceResult;
    int count;
    private RequestQueue mQueue;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.result_page);
        companyNameResult = (TextView) findViewById(R.id.CompanyName);
        positionNameResult = (TextView) findViewById(R.id.position);
        salaryResult = (TextView) findViewById(R.id.salary);
        addressResult = (TextView) findViewById(R.id.Address);
        housePriceResult = (TextView) findViewById(R.id.Price);
        companyNameResult.setText(MainActivity.companyName);
        positionNameResult.setText(MainActivity.jobTitle);
        salaryResult.setText(MainActivity.salary);
        addressResult.setText(MainActivity.address);
        housePriceResult.setText(MainActivity.price);


        View button = (Button) findViewById(R.id.back);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                Intent newIntent = new Intent(resultPage.this, MainActivity.class);
                startActivity(newIntent);
            }
        });

    }
}


package com.example.testchaquopy;

//import static com.example.testchaquopy.R.id.text;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.EditText;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    TextView display;
    EditText Textbox;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Textbox=(EditText) findViewById(R.id.Textbox);
        display=(TextView) findViewById(R.id.display);


        //text= (TextView) findViewById(R.id.text);
        //if (! Python.isStarted()) {
        //    Python.start(new AndroidPlatform(this));
        //}
        //Python py=Python.getInstance();
        //PyObject pyobj=py.getModule("myscript");
        //PyObject obj=pyobj.callAttr("main");
        //text.setText(obj.toString());
    }
    public void calculate(View v)
    {
        InputMethodManager imm = (InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(v.getApplicationWindowToken(),0);
        String ciffile1=Textbox.getText().toString();
        if (! Python.isStarted()) {
              Python.start(new AndroidPlatform(this));
            }
            Python py=Python.getInstance();
            PyObject pyobj=py.getModule("hbond");
            PyObject obj=pyobj.callAttr("distance",ciffile1);
            display.setText(obj.toString());

    }

}
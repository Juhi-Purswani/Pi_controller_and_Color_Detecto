package com.example.android.picontroller;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {
    private Button forward ;
    private Button backward ;
    private Button right ;
    private Button left ;
    private EditText ipAddress;

    Socket myAppSocket = null;
    public static String wifiModuleIp = "";
    public static int wifiModulePort = 0;
    public static String CMD = "0";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        forward = (Button)findViewById(R.id.btn_forward);
        backward = (Button)findViewById(R.id.btn_backward);
        right = (Button)findViewById(R.id.btn_right);
        left = (Button)findViewById(R.id.btn_left);

        ipAddress = (EditText)findViewById(R.id.ipAdress);

        forward.setOnCreateContextMenuListener(new View.OnCreateContextMenuListener() {
            @Override
            public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
                getIpAndPort();
                CMD = "forward";
                Socket_AsyncTask cmd_forward_server = new Socket_AsyncTask();
                cmd_forward_server.execute();
            }
        });

        backward.setOnCreateContextMenuListener(new View.OnCreateContextMenuListener() {
            @Override
            public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
                getIpAndPort();
                CMD = "backward";
                Socket_AsyncTask cmd_backward_server = new Socket_AsyncTask();
                cmd_backward_server.execute();
            }
        });

        right.setOnCreateContextMenuListener(new View.OnCreateContextMenuListener() {
            @Override
            public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
                getIpAndPort();
                CMD = "right";
                Socket_AsyncTask cmd_right_server = new Socket_AsyncTask();
                cmd_right_server.execute();
            }
        });

        left.setOnCreateContextMenuListener(new View.OnCreateContextMenuListener() {
            @Override
            public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
                getIpAndPort();
                CMD = "left";
                Socket_AsyncTask cmd_left_server = new Socket_AsyncTask();
                cmd_left_server.execute();
            }
        });
    }

    public void getIpAndPort(){
        String ipAndPort = ipAddress.getText().toString();
        String temp[] = ipAndPort.split(":");
        wifiModuleIp = temp[0];
        wifiModulePort = Integer.valueOf(temp[1]);
    }

    public class Socket_AsyncTask extends AsyncTask<Void,Void,Void>{
        Socket socket;

        @Override
        protected Void doInBackground(Void... params) {
            try{
                InetAddress inetAddress = InetAddress.getByName(MainActivity.wifiModuleIp);
                socket = new java.net.Socket(inetAddress,MainActivity.wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeBytes(CMD);
                dataOutputStream.close();
                socket.close();
            }catch (UnknownHostException e){
                e.printStackTrace();
            } catch (IOException e ){
                e.printStackTrace();
            }
            return null;
        }
    }
}

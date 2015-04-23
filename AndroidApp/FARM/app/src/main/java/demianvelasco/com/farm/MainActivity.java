package demianvelasco.com.farm;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.firebase.client.DataSnapshot;
import com.firebase.client.Firebase;
import com.firebase.client.FirebaseError;
import com.firebase.client.ValueEventListener;

import org.w3c.dom.Text;


public class MainActivity extends ActionBarActivity {


    String lat = "0.0";
    String lon = "0.0";

    private static final long MINIMUM_DISTANCE_CHANGE_FOR_UPDATES = 1; // in Meters
    private static final long MINIMUM_TIME_BETWEEN_UPDATES = 1000; // in Milliseconds
    protected LocationManager locationManager;

    EditText moduleIDText;





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Firebase.setAndroidContext(this);

        final Firebase ref = new Firebase("https://farmsd.firebaseio.com/coordinates/");


        moduleIDText = (EditText) findViewById(R.id.moduleID);

        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                MINIMUM_TIME_BETWEEN_UPDATES,
                MINIMUM_DISTANCE_CHANGE_FOR_UPDATES,
                new MyLocationListener()
        );



        final ImageButton plantButton = (ImageButton) findViewById(R.id.plantButtonIcon);
        plantButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addLocationToDatabase(ref);
            }
        });
    }

    protected void addLocationToDatabase(Firebase ref) {

        Location location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);

        String moduleID = moduleIDText.getText().toString();

        if (location != null) {
                    lat =  Double.toString(location.getLatitude());
                    lon =  Double.toString(location.getLongitude());
        }

        if (moduleID.equals("A") || moduleID.equals("B") || moduleID.equals("C") || moduleID.equals("D") || moduleID.equals("E")) {
            Toast.makeText(getApplicationContext(), "Module " + moduleID + "  Lat:  " + lat + "  Lon:  " + lon, Toast.LENGTH_LONG).show();
            ref.child(moduleID).child("lon").setValue(lon);
            ref.child(moduleID).child("lat").setValue(lat);
            moduleIDText.setText("");
        } else {
            new AlertDialog.Builder(this)
                    .setTitle("Module Offline")
                    .setMessage("The module you've chosen is offline. FARM on")
                    .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int which) {
                            // continue with delete
                            moduleIDText.setText("");
                        }
                    })
                    .setIcon(android.R.drawable.ic_dialog_alert)
                    .show();

        }
    }

    private class MyLocationListener implements LocationListener {
        public void onLocationChanged(Location location) {


        }
        public void onStatusChanged(String s, int i, Bundle b) {

        }
        public void onProviderDisabled(String s) {
            Toast.makeText(MainActivity.this,
                    "Provider disabled by the user. GPS turned off",
                    Toast.LENGTH_LONG).show();
        }
        public void onProviderEnabled(String s) {

            Toast.makeText(MainActivity.this,
                    "Provider enabled by the user. GPS turned on",
                    Toast.LENGTH_LONG).show();
        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using GoogleARCore;
using UnityEngine.UI;
using TMPro;

public class TextController : MonoBehaviour
{
    public Camera firstPersonCamera;
    private Anchor anchor;
    private DetectedPlane detectedPlane;
    private float yOffset;
    public TextMeshPro mytext = null;
    int id = 0;

    // Start is called before the first frame update
    void Start()
    {
        if (id == 0)
        {
            mytext.text = "Voedingswaarden			per 100g Energetische waarde: 		1528kJ / 364kcal Vet: 					3.6g waarvan verzadigde vetzuren:  1.2g Koolhydraten:			46.7g waarvan suikers: 1.4g Vezels:				3.3g Eiwitten:				34.4g Zout:					1.38g";
        }
        foreach (Renderer r in GetComponentsInChildren<Renderer>())
        {
            r.enabled = false;
        }
    }

    // Update is called once per frame
    void Update()
    {
        // The tracking state must be FrameTrackingState.Tracking in order to access the frame
        if (Session.Status != SessionStatus.Tracking)
        {
            return;
        }

        // If there is no plane, then return
        if (detectedPlane == null)
        {
            return;
        }

        // Check for the plane being subsumed
        // If the plane has been subsumed switch attachment to the subsuming plane
        while (detectedPlane.SubsumedBy != null)
        {
            detectedPlane = detectedPlane.SubsumedBy;
        }

        // Make the scoreboard face the viewer
        transform.LookAt(firstPersonCamera.transform);

        // Move the positiion to stay consistent with the plane
        transform.position = new Vector3(transform.position.x, detectedPlane.CenterPose.position.y + yOffset, transform.position.z);

    }

    public void SetSelectedPlane(DetectedPlane detectedPlane)
    {
        this.detectedPlane = detectedPlane;
        CreateAnchor();
    }

    private void CreateAnchor()
    {
        // Create the position of the anchor by raycasting a point towards the top of the screen
        Vector2 pos = new Vector2(Screen.width * .5f, Screen.height * .5f);
        Ray ray = firstPersonCamera.ScreenPointToRay(pos);
        Vector3 anchorPosition = ray.GetPoint(5f);

        // Create the anchor at that point
        if (anchor != null)
        {
            Destroy(anchor);
        }
        else if (anchor == null)
        {
            anchor = detectedPlane.CreateAnchor(new Pose(anchorPosition, Quaternion.identity));
        }

        // Attach the scoreboard to the anchor
        transform.position = anchorPosition;
        transform.SetParent(anchor.transform);

        // Record the y offset from the plane
        yOffset = transform.position.y - detectedPlane.CenterPose.position.y;

        // Enable the renderers
        foreach (Renderer r in GetComponentsInChildren<Renderer>())
        {
            r.enabled = true;
        }

    }

}

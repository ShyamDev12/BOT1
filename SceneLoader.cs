using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneLoader : MonoBehaviour
{
    public void LoadAnalytics(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }
}